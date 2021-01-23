# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/sample.css' %}">
    <link rel = "icon" href ="{% static 'img/titleicon.jpg' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
        Silicon Private Limited.
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/people">people</a></div>
        <div class="menuitem"><a href="/products">products</a></div> 
        <div class="menuitem"><a href="/contactus">contactus</a></div>
        
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2021 Silicon Private Limited, Developed by bhavya.
    </div>
    </div>
</body>

</html>
```

### home.html
```
{% extends "websitedynamic/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/building2.jpg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}
```
### people.html
```
{% extends "websitedynamic/base.html" %}

{% block content %}

<div class="content">
    <div class="people">
        {% for people in peoples %}
        <div class="crew">
            <div class="personimage">
                <img src="{{ people.photo.url }}" alt="Person Photo">
            </div>
            <div class="personname">{{ people.name }}</div>
            <div class="designation">Designation: {{ people.designation }}</div>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock  %}
```
### products.html
```
{% extends "websitedynamic/base.html" %}
{% block content %}

<div class="content">
    <div class="productsitems">
        {% for products in productss %}
        <div class="productsitem">
            <div class="itemimage">
                <img src="{{ products.photo1.url }}" alt="Item Photo1">
            </div>
            <div class="itemname">{{ products.name }}</div>
            <div class="itemprice">Price: {{ products.price }}</div>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock  %}
```
### contactus.html
```

{% extends "websitedynamic/base.html" %}

{% block content %}
<div class="contactuscontent">
    <h1>CONTACT US</h1>
    <div class="contactustext">
        <h2> PRASAD (General Contact Manager),</h2>
        <h2> M. K. Silicon Products Private Limited,</h2>
        <h2> ilabs India Private Limited 9th Floor, Maximus Towers 2B, Raheja Mindspace IT Park, APIIC Software Layout,
            Madhapur, Hyderabad,</h2>
        <h2> Telangana, India - 500081,</h2>
        <h2> contact number-91-40-39351000</h2>
        <h2> Email address-Silicon@gmail.com</h2>

    </div>

</div>
{% endblock  %}
```
## OUTPUT:
![output](./static/img/output1.jpg)

![output](./static/img/output2.jpg)

![output](./static/img/output3.jpg)

![output](./static/img/output4.jpg)

## CODE VALIDATION REPORT:
![output](./static/img/report1.jpg)

![output](./static/img/report2.jpg)

![output](./static/img/report3.jpg)

![output](./static/img/report4.jpg)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://bhavya.student.saveetha.in:8000/. HTML code is validated.