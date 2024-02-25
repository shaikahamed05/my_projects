<%@include file="connect.jsp" %>
<%
    String id=request.getParameter("id1");
    String name=request.getParameter("name1");
    String gmail=request.getParameter("gmail1");
    String psw=request.getParameter("psw1");
    String num=request.getParameter("num1");
    String doj=request.getParameter("doj");
    String dob=request.getParameter("dob");
    
    String sql="insert into staff values("+id+",'"+name+"','"+gmail+"','"+psw+"','"+num+"','"+doj+"','"+dob+"')";
    st.executeUpdate(sql);
%>
<script>
    window.alert("Staff added Sucessfully..");
    window.location.assign("AdminHomePage.jsp");
</script>