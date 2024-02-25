<%@include file="connect.jsp" %>
<%
    String id=request.getParameter("t1");
    String name=request.getParameter("t2");
    String email=request.getParameter("t3");
    String psw1=request.getParameter("t4");
    String num1=request.getParameter("t5");
    String doj=request.getParameter("t7");
    String dob=request.getParameter("t8");
    
    String sql="update staff set email='"+email+"',password='"+psw1+"',contact='"+num1+"' where staffid='"+id+"'";
    st.executeUpdate(sql);
%>
<script>
    window.alert("Staff Updated Sucessfully..");
    window.location.assign("staffprofile.jsp");
</script>