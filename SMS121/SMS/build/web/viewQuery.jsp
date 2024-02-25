<%@include file="connect.jsp" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
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
    <li><a class="active" href="StaffHomePage.jsp">Home</a></li>
  <li><a href="staffprofile.jsp">Staff Profile</a></li>
  <li><a href="updateQuery.jsp">Query</a></li>
  
  <li style="float:right"><a href="home.html">Logout</a></li>
</ul>
<center><h2>Student Details</h2></center>
        <%
            ResultSet rs=st.executeQuery("Select * from query where result is null");
            ResultSetMetaData rsmd=rs.getMetaData();
            int cc=rsmd.getColumnCount();
            %>
            <table width=1000 align="center" border="1" style="background-color: powderblue;">
                <tr>
                    <%
                        for(int i=1;i<=cc;i++)
                        {
                            %>
                            <td><%=rsmd.getColumnLabel(i)%> </td>
                            <%
                        }
                         %>
                         <td>Update</td><td>Delete</td>
                         <%
                        while(rs.next())
                        {
                            %>
                            <tr>
                                    <%
                                for(int i=1;i<=cc;i++)
                                {
                                    %>
                                    <td><%=rs.getString(i)%> </td>
                                    <%
                                }
                                 %>
                                 <td><a href="updateQuery.jsp?qid=<%=rs.getString(1)%>">Answer</a></td>
                                 
                            </tr>
                            <%
                        }
                        %>
                </tr>
                
            </table>
    </body>
</html>
