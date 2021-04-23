# HTML 入门

## HTML 使用元素来描述页面

```html
<html>
    <body>
        <h1>This is a title. </h1>
        <p>这是 p 标签，用于包裹一个段落的内容。</p>
    </body>
</html>
```

## 标签的特性（属性）

```html
<p style="color:red">...</p>
```

## 常用的标签（1） body head

```html
<html>
    <head></head>
    <body>
        <h1>Hello HTML!</h1>
    </body>
</html>
```

## 常用的标签（2） h1 - h6

```html
<html>
    <head></head>
    <body>
        <h1>Hello HTML!</h1>
        <h2>Hello HTML!</h2>
        <h3>Hello HTML!</h3>
        <h4>Hello HTML!</h4>
        <h5>Hello HTML!</h5>
        <h6>Hello HTML!</h6>
    </body>
</html>
```

## 常用的标签（3） ol ul li

```html
<ol>
    <li>有序列表项目1</li>
    <li>有序列表项目2</li>
    <li>有序列表项目3</li>
</ol>

<ul>
    <li>无序列表项目1</li>
    <li>无序列表项目2</li>
    <li>无序列表项目3</li>
</ul>
```

## 常用的标签（4）

```html
<a href="http://www.baidu.com">点击打开百度</a>
```

```html
<img src="https://7n.w3cschool.cn/statics/images/logonew2.png" />
```

## 常用的标签（5） table tr th td

```html
<table>
    <tr>
        <th></th>
        <th>星期六</th>
	    <th>星期日</th>
    </tr>
    <tr>
        <th>门票售出量</th>
        <td>120</td>
        <td>135</td>
    </tr>
    <tr>
        <th>销售额</th>
        <td>$600</td>
        <td>$675</td>
    </tr>
</table>
```

## 常用的标签（6） input textarea

```html
<input type="text" placeholder="提示词" />
<input type="password" value="value" />
<input type="submit" />
<input type="file" />
<input type="radio" />
<input type="checkbox" />
```

```html
<textarea></textarea>
```

## 常用的标签（7） select option form

```html
<select>
    <option value="0">请选择内容</option>
    <option value="1">第一个选项</option>
    <option value="2">第二个选项</option>
</select>
```

## 注释

```html
<!-- 注释的内容 -->
```

# CSS 介绍

## CSS 简介

```css
p {
    color: #565656;
}
```

## 在 HTML 中引入 CSS 样式

```html
<html>
    <head>
        <link href="css/style.css" type="text/css" rel="stylesheet" />
    </head>
    <body></body>
</html>
```

```css
body, a{
    overflow-x: overlay;
    padding: 0 !important;
}

.hide_scroll{
    overflow: hidden !important;
}
```

## 在 HTML 中引入 CSS 样式

```html
<html>
    <head>
        <style>
            body, a {
                padding: 0;
            }
        </style>
    </head>
    <body></body>
</html>
```

```html
<a style="text-decoration: none;">example</a>
```

# JavaScript 基础与 DOM

## JavaScript 毒瘤：==

```js
'' == '0'               // false
0 == ''                 // true
0 == '0'                // true

false == 'false'        // false
false == 0              // true
null == undefined       // true

'\n' == 0               // true
'\t' == 0               // true
'\r\n' == 0             // true

0.1 + 0.2 == 0.3        // false
```

## JavaScript 对象、函数

```js
var object = {
    name: 'JavaScript',
    age: 15,
    'like JavaScript': true
};
```

```js
object.name;

object['like JavaScript'];

object.sex;	// undefined
```

```js
function add(a, b) {
    return a + b;
}

var add = function(a, b) {
    return a + b;
};

add(0, 1);
```

```js
function(a, b) {
    return a + b;
}
```

```js
var object = {
    func1: function() {
        ...
    },

    func2() {
        ...
    }
};
```

## JavaScript 数组

```js
var arr = [1, 'JavaScript', {}];

var arr = new Array(10);
```

```js
arr[1];
arr.push(0.6);
arr.indexOf(1);
arr.sort(function(a, b) {
    return a – b;
});
arr = arr.concat([2, 3]);
arr.length;
```

## 函数调用模式与 this 变量（1）

```js
var object = {
    age: 18,
    func: function() {
        this.age;
    }
};

object.func();
```

## 函数调用模式与 this 变量（2）

```js
var func = function() {
    this;
};

func();
```

## 函数调用模式与 this 变量（3）

```js
var func = function(params) {
    this.age;
};

var object = {
    age: 18,
};

func.apply(object, 1);
```

## JavaScript 毒瘤 2：this 变量的设计

```js
function gloFunction(f) {
    var age = 17;
    f();
}

var object = {
    age: 18,
    func: function() {
        gloFunction(function() {
            console.log(this.age);
        });
    }
};

object.func();
```

```js
func: function() {
    var that = this;
    gloFunction(function() {
        console.log(that.age);
    });
}
```

## 将 JavaScript 引入 HTML

```html
<html>
    <head>
        <script src="js/index.js"></script>    
    </head>
    <body></body>
</html>
```

```html
<html>
    <head>
        <script>
	        // ...
        </script>    
    </head>
    <body></body>
</html>
```

## HTML DOM

```html
<a
    id="openBaidu" 
    class="link-a"
    href="http://www.baidu.com">
    点击打开百度
</a>
```

```js
var a = document.createElement('a');
a.id = 'openBaidu';
a.classList.add('link-a');
a.setAttribute('href', 'http://www.baidu.com');
a.innerHTML = '点击打开百度';
parentNode.appendChild(a);
```

```js
parentNode.getElementById('openBaidu');
parentNode.getElementsByTagName('a');
parentNode.getElementsByClassName('link-a');

document.getElementsByClassName('link-a');
```

## innerHTML 的使用

```html
<ul id="nav"></ul>
```

```js
document.getElementById('nav').innerHTML = '<li>index</li>';

document.getElementById('nav').textContent = '<li>index</li>';
```

## 设置监听器

```js
document.getElementById('openBaidu').addEventListener('click', function(){
    // ...
});

document.getElementById('openBaidu').removeEventListener('click', myFunction);
```

## DOM 加载与 JavaScript 执行时机

```html
<script>
    document.getElementById('mid');
</script>
<div id="mid"></div>
```

```html
<script>
    window.onload = function() {
        document.getElementById('mid');
    };
</script>
<div id="mid"></div>
```

## alert 与 console

```js
alert('这是一个提示');

console.log('控制台信息');
console.warn('控制台信息');
console.error('控制台信息');
```
