<%@include file="connect.jsp" %>
<%
    String id=request.getParameter("id");
    String name=request.getParameter("name");
    String email=request.getParameter("email");
    String psw1=request.getParameter("psw");
    String num1=request.getParameter("num");
    String branch=request.getParameter("branch");
    String doa=request.getParameter("doa");
    String dob=request.getParameter("dob");
    
    String sql="insert into student values("+id+",'"+name+"','"+email+"','"+psw1+"','"+num1+"','"+branch+"','"+doa+"','"+dob+"')";
    st.executeUpdate(sql);
%>
<script>
    window.alert("Student added Sucessfully..");
    window.location.assign("AdminHomePage.jsp");
</script>