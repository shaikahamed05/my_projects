<%
  String un=request.getParameter("uname");
  String pwd=request.getParameter("psw");
  if(un.equals("admin") && pwd.equals("admin"))
  {
      %>
      <script>
          window.alert("Login Success...")
          window.location.assign("AdminHomePage.jsp")
      </script>
      <%
      
  }
  else
  {
    %>
    <jsp:include page="adminLogin.html"/>
    <center><h2 style="color:red">UserName/password Not Match</h2></center>
    <%
  }
%>