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
        String id=request.getParameter("qid");
        String sql="select * from query  where qid="+id;
        ResultSet rs=st.executeQuery(sql);
        rs.next();
        %>
    <table>
        <caption><h2 style="color:violet;">Student Details</h2></caption>
        <form method="get" action="updateQueryDB.jsp">
            <tr><td>id</td><td><input type="text" name="id" value=<%=rs.getString(1)%> readonly=""></td></tr>
            <tr><td>Query</td><td><textarea  rows=5 cols=80 readonly=""><%=rs.getString(2)%></textarea></td></tr>
            <tr><td>Answer</td><td><textarea name="ans" rows="10" cols="80"></textarea></td></tr>
            
            <tr><td colspan="2" align="center"><input type="submit" value="updateQuery"></td></tr>
        </form>
    </table>
</center>

</body>
</html>


