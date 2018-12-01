# 第8章 多线程编程核心技术应用进阶训练
## 8-1 如何使用多线程 
![8-1.png](https://i.loli.net/2017/11/13/5a0941f90a488.png)
![8-1-1.png](https://i.loli.net/2017/11/13/5a0942d5a791a.png)
![8-1-2.png](https://i.loli.net/2017/11/13/5a0943555620f.png)

## 8-2 如何线程间通信 
![8-2-1.png](https://i.loli.net/2017/11/13/5a09473cf166c.png)
#### ConvertThread 类的 run 方法
![8-2-2.png](https://i.loli.net/2017/11/13/5a09473c997ef.png)
![8-2-3.png](https://i.loli.net/2017/11/13/5a09473c9e210.png)

## 8-3 如何在线程间进行事件通知 
![8-3.png](https://i.loli.net/2017/11/13/5a09498e24cb3.png)
### 压缩打包
![8-3-tip.png](https://i.loli.net/2017/11/13/5a09498e0e4d7.png)
### Event.wait() && Event.set()
![Event](https://i.loli.net/2017/11/13/5a09498e0c46a.png)

## 8-4 如何使用线程本地数据
![8-4.png](https://i.loli.net/2017/11/22/5a156275035b7.png)
<pre>
    import os, cv2, time, struct, threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import TCPServer, ThreadingTCPServer
from threading import Thread, RLock
from select import select

class JpegStreamer(Thread):
    def __init__(self, camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self, pr):
        self.lock.acquire()
        self.pipes.pop(pr)
        self.lock.release()
        pr.close()
        pw.close()

    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                #ret, data = cv2.imencode('.jpg', frame)
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.tostring()

    def send(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.itervalues(), [], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send(frame)

class JpegRetriever(object):
    def __init__(self, streamer):
        self.streamer = streamer
        self.local = threading.local()

    def retrieve(self):
        while True:
            ns = os.read(self.local.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.local.pipe, n)
            yield data

    def __enter__(self):
        if hasattr(self.local, 'pipe'):
            raise RuntimeError()

        self.local.pipe = streamer.register()
        return self.retrieve()

    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True

class Handler(BaseHTTPRequestHandler):
    retriever = None
    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever

    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')

        if self.path != '/':
            return

        self.send_response(200) 
        self.send_header("Content-type", 'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()

        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)

    def send_frame(self, frame):
        self.wfile.write('--abcde\r\n')
        self.wfile.write('Content-Type: image/jpeg\r\n')
        self.wfile.write('Content-Length: %d\r\n\r\n' % len(frame))
        self.wfile.write(frame)

if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()

    retriever = JpegRetriever(streamer)
    Handler.setJpegRetriever(retriever)

    print 'Start server...'
    httpd = ThreadingTCPServer(('', 9000), Handler)
    httpd.serve_forever()
</pre>

## 8-5 如何使用线程池 
![8-5.png](https://i.loli.net/2017/11/22/5a15633b06d31.png)

## 8-6 如何使用多进程
![8-6.png](https://i.loli.net/2017/11/22/5a15668816779.png)
![8-6-1.png](https://i.loli.net/2017/11/22/5a15671180e5e.png)
![8-6-2.png](https://i.loli.net/2017/11/22/5a156751aa5dc.png)
