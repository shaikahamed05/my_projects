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

.logo1{
	font-size: 1em;
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

body1{
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    display: flex;
    justify-content: center;
    align-items: center;
}

.formBox{
    display: flex;
    position: relative;
    padding: 50px;
    width: 500px;
    height: 350px;
    background: transparent;
    justify-content: center;
    border: 2px solid white;
    border-radius: 20px;
    backdrop-filter: blur(3px);
}

</style>
</head>
<body bgcolor="#000000">
<br><center><h1 class="logo">Student Management System</h1></center><br>
<ul>
    <li><a class="active" href="AdminHomePage.jsp">Home</a></li>
  <li><a href="addStaff.jsp">AddStaff</a></li>
  <li><a href="viewStaff.jsp">ViewStaff</a></li>
  <li><a href="addStudent.jsp">AddStudent</a></li>
  <li><a href="viewStudent.jsp">ViewStudent</a></li>
  <li style="float:right"><a href="home.html">Logout</a></li>
</ul>

<br><br><body1>
<div class="formBox">
		<div>
		<center>
		<table>
			<center><h2 class="logo">Student Details</h2></center><br>
        		<form method="get" action="addStudentDB.jsp">
            		<tr><td class="logo1">Student ID:</td><td><input type="text" name="id" required=""></td></tr>
                        <tr><td class="logo1">Name:</td><td><input type="text" name="name" required=""></td></tr>
                        <tr><td class="logo1">Email:</td><td><input type="text" name="email" required=""></td></tr>
                        <tr><td class="logo1">Password:</td><td><input type="text" name="psw" required=""></td></tr>
                        <tr><td class="logo1">Contact Number:</td><td><input type="text" name="num" required=""></td></tr>
                        <tr><td class="logo1">Branch:</td><td><input type="text" name="branch" required=""></td></tr>
                        <tr><td class="logo1">DOA:</td><td><input type="date"  style="width:165px" name="doa" required=""></td></tr>
                        <tr><td class="logo1">DOB:</td><td><input type="date"  style="width:165px" name="dob" required=""></td></tr>
                        <tr><td colspan="2" align="center"><input type="submit" value="AddStudent"></td></tr>
        		</form>
		<table>
		</center>
		</div>
</div>
</body1>

</body>
</html>


