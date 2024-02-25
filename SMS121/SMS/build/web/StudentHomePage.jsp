<!DOCTYPE html>
<html>
<head>
<style>
    
@import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');

*{
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Rubik',swap;
}

.logo{
	font-size: 2em;
	color: #fff;
	user-select:none;
}    
    
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
  border-right:1px solid #bbb;
}

li:last-child {
  border-right: none;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>
<br><center><h1>Student Management System</h1></center><br>
<ul>
    <li><a class="active" href="StudentHomePage.jsp">Home</a></li>
  <li><a href="studentprofile.jsp">Student Profile</a></li>
  <li><a href="Query.jsp">Query</a></li>
  
  <li style="float:right"><a href="home.html">Logout</a></li>
</ul>
<br><center><h1>Name is  :<%=session.getAttribute("name")%></center><br>
</body>
</html>


