# TypeScript入门
![](http://img.mukewang.com/583fcefd0001c1c906000338.jpg "TypeScript 入门")

### 字符串新特性
- 自动拆分字符串

当使用字符串模板去调用方法时，字符串模板中的表达式的值会自动赋给被调用方法的参数。

```typescript
function test(template, name, age){
	console.log(template); 
	console.log(name); 
	console.log(age); 
}

var myname = "Lewis Tian"; 

var getAge = function(){
	return 18; 
}

test`hello my name is ${myname},i'm ${getAge()}`
```

运行结果如下
```javascript
[ 'hello my name ig ', ',i\'m ', '' ]
Lewis Tian
18
```

### 参数新特性
- 自定义参数类型

```typescript
class Person {
	name:string; 
	age:number;
}
```

- 函数参数默认值

```typescript
var myname: string = "Lewis Tian"; 
function test(a: string,b: string, c: string = "jojo") {
	console.log(a); 
	console.log(b); 
	console.log(c); 
}

test("xxx","yyy","zzz"); // "xxx" "yyy" "zzz"
test("xxx","yyy"); // "xxx" "yyy" "jojo"
```

- 可选参数

```typescript
var myname: string = "Lewis Tian"; 
function test(a: string,b?: string, c: string = "jojo") {
	console.log(a); 
	console.log(b); 
	console.log(c); 
}

test(myname); // "Lewis Tian" undefined "jojo"
```

### 函数新特性
- Rest and Spread 操作符

用来声明任意数量的方法参数

```typescript
function func1(...args){
	args.forEach(function (arg) {
		console.log(arg);
	})
}

func1(1,2,3); 

func1(7,8,9,10,11);
```

把任意长度的数组传入固定参数的方法

```typescript
function func1(a, b, c){
	console.log(a);
	console.log(b); 
	console.log(c); 
}

var args = [1,2]; 
func1(...args); 

var args2 = [7,8,9,10,11]; 
func1(...args2);
```

- generator 函数

控制函数的执行过程，手工暂停和恢复代码执行

```typescript
function* doSomething(){
	console.log("start");
	yield; 
	console.log("finish");
}
var func1 = doSomething(); 

func1.next(); // "start"
func1.next(); // "finish" 
```

```typescript
function* getStockPrice(stock){
	while(true){
		yield Math.random()*100;
	}
}

var priceGenerator =getStockPrice("IBM"); 

var limitPrice=15; 
var price=100; 

while(price>limitPrice){
	price=priceGenerator.next().value; 
	console.log(`the generator return ${price}`);
}
```

- destructuring 析构表达式

通过表达式将对象或数组拆解成任意数量的变量

```typescript
function getStock(){
	return {
		code: "IBM", 
		price: {
			price1: 200,
			price2: 200,
		}
	}
}

var {code, price} = getStock();

var {code: codex, price: {price1}} = getStock();

console.log(codex, price1)

var {codex, price} = getStock(); // erro
```

```
var arr = [1, 2, 3, 4];

var [num1, num2, , num4] = arr;
```

### 表达式和循环
- 箭头表达式

用来声明匿名函数，消除传统匿名函数的 this 指针问题

```typescript
function getStock(name: string){
	this.name = name; 
	setInterval(function(){
		console.log("getStock name is:"+this.name);
	},1000);
}

function getStock2(name: string){
	this.name = name; 
	setInterval(()=>{
		console.log("getStock2 name is:"+this.name);
		},1000);
}

var stock = new getStock("IBM"); // getStock name is:undefined
var stock2 = new getStock2("IBM"); // getStock2 name is:IBM
```

### 面向对象特性
- 接口

```typescript
interface IPerson{
	name:string; 
	age:number;
} 

class Person{
	constructor(public config:IPerson){
	
	}
}

var pl = new Person({
	name:"zhangsan", 
	age:18
});
```

```
interface Animal{
	eat(); 
}

class Sheep implements Animal{
	eat(){
		console.log("i eat grass"); 
	}
}

class Tiger implements Animal{
	eat(){
		console.log("i eat meat");
	}
}
```