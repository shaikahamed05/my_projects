<%@include file="connect.jsp" %>
<!DOCTYPE html>
<html>
<head>
<style>
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
<center><h1>Student Management System</h1></center>
<ul>
    <li><a class="active" href="AdminHomePage.jsp">Home</a></li>
  <li><a href="addStaff.jsp">AddStaff</a></li>
  <li><a href="viewStaff.jsp">ViewStaff</a></li>
  <li><a href="addStudent.jsp">AddStudent</a></li>
  <li><a href="viewStudent.jsp">ViewStudent</a></li>
  <li style="float:right"><a href="home.html">Logout</a></li>
</ul>

<center>
    <%
        String id=request.getParameter("sid");
        String sql="select * from student  where studentid="+id;
        ResultSet rs=st.executeQuery(sql);
        rs.next();
        %>
    <table>
        <caption><h2 style="color:violet;">Student Details</h2></caption>
        <form method="get" action="updateStudentDB.jsp">
            <tr><td>id no</td><td><input type="text" name="id" value=<%=rs.getString(1)%> readonly=""></td></tr>
            <tr><td>name</td><td><input type="text" name="name" value=<%=rs.getString(2)%> readonly=""></td></tr>
            <tr><td>email</td><td><input type="text" name="email"  value=<%=rs.getString(3)%> required=""></td></tr>
            <tr><td>password</td><td><input type="text" name="psw"  value=<%=rs.getString(4)%> required=""></td></tr>
            <tr><td>number</td><td><input type="text" name="num"  value=<%=rs.getString(5)%> required=""></td></tr>
            <tr><td>branch</td><td><input type="text" name="branch"  value=<%=rs.getString(6)%> required=""></td></tr>
          <tr><td>DOA</td><td><input type="date"  style="width:165px" name="doa"  value=<%=rs.getString(7)%> required=""></td></tr>
            <tr><td>DOB</td><td><input type="date"  style="width:165px" name="dob"  value=<%=rs.getString(8)%> required=""></td></tr>
            <tr><td colspan="2" align="center"><input type="submit" value="updateStudent"></td></tr>
        </form>
    </table>
</center>

</body>
</html>


