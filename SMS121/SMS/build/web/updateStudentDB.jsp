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
    
    String sql="update student set email='"+email+"',password='"+psw1+"',contact='"+num1+"',branch='"+branch+"',doa='"+doa+"',dob='"+dob+"' where studentid="+id;
    System.out.println("Sql "+sql);
    st.executeUpdate(sql);
%>
<script>
    window.alert("Student Updated Sucessfully..");
    window.location.assign("viewStudent.jsp");
</script>