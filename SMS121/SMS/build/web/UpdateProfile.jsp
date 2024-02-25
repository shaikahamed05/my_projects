<%@include file="connect.jsp" %>
<%
    String id=request.getParameter("t1");
    String name=request.getParameter("t2");
    String email=request.getParameter("t3");
    String psw1=request.getParameter("t4");
    String num1=request.getParameter("t5");
    String branch=request.getParameter("t6");
    String doa=request.getParameter("t7");
    String dob=request.getParameter("t8");
    
    String sql="update student set email='"+email+"',password='"+psw1+"',contact='"+num1+"' where studentid='"+id+"'";
    st.executeUpdate(sql);
%>
<script>
    window.alert("Student Updated Sucessfully..");
    window.location.assign("studentprofile.jsp");
</script>