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
        String sql="select * from staff where staffid="+id;
        ResultSet rs=st.executeQuery(sql);
        rs.next();
        %>
    <table>
        <caption>Staff Details</caption>
        <form method="get" action="updateStaffDB.jsp">
            <tr><td>Staff ID</td><td><input type="text" name="id1" value=<%=rs.getString(1)%> readonly=""></td></tr>
            <tr><td>Name</td><td><input type="text" name="name1" value=<%=rs.getString(2)%>   readonly=""></td></tr>
            
            <tr><td>Email</td><td><input type="email" name="gmail1"  value=<%=rs.getString(3)%> required=""></td></tr>
            <tr><td>password</td><td><input type="text" name="psw1" value=<%=rs.getString(4)%>  required=""></td></tr>
            <tr><td>Contact number</td><td><input type="text" name="num1"  value=<%=rs.getString(5)%> required=""></td></tr>
            <tr><td>DOJ</td><td><input type="date" name="doj" style="width:165px"  value=<%=rs.getString(6)%> required=""></td></tr>
            <tr><td>DOB</td><td><input type="date" name="dob"  style="width:165px"  value=<%=rs.getString(7)%> required=""></td></tr>
            <tr><td colspan="2" align="center"><input type="submit" value="UpdateStaff"></td></tr>
        </form>
    </table>
</center>

</body>
</html>


