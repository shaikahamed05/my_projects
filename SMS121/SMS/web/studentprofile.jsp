n <%@include file="connect.jsp" %>
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
<center><table align="center" border="1" bgcolor="lightblue">
<%
    String sid=session.getAttribute("sid").toString();
    String sql="select * from student where studentid='"+sid+"'";
    ResultSet rs=st.executeQuery(sql);
    ResultSetMetaData rsmd=rs.getMetaData();
    int cc=rsmd.getColumnCount();
    rs.next();
    
        %>
        <form method="get" action="UpdateProfile.jsp">
        <tr><td><%=rsmd.getColumnLabel(1)%></td><td><input type="text" name="t1" value="<%=rs.getString(1)%>" readonly=""></td></tr>
        <tr><td><%=rsmd.getColumnLabel(2)%></td><td><input type="text" name="t2" value="<%=rs.getString(2)%>" readonly=""></tr>
        <tr><td><%=rsmd.getColumnLabel(3)%></td><td><input type="text" name="t3" value="<%=rs.getString(3)%>" required=""></tr>
        <tr><td><%=rsmd.getColumnLabel(4)%></td><td><input type="text" name="t4" value="<%=rs.getString(4)%>" required=""></td></tr>
        <tr><td><%=rsmd.getColumnLabel(5)%></td><td><input type="text" name="t5" value="<%=rs.getString(5)%>" required=""></td></tr>
        <tr><td><%=rsmd.getColumnLabel(6)%></td><td><input type="text" name="t6" value="<%=rs.getString(6)%>" readonly=""></td></tr>
        <tr><td><%=rsmd.getColumnLabel(7)%></td><td><input type="text" name="t7" value="<%=rs.getString(7)%>" readonly=""></td></tr>
        <tr><td><%=rsmd.getColumnLabel(8)%></td><td><input type="text" name="t8" value="<%=rs.getString(8)%>" readonly=""></td></tr>
        <tr><td colspan="2" align="center"><input type="submit" value="Update"></td></tr>
        </form></center>
        <%
    %>
    </table>
</body>
</html>


