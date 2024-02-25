<%@include file="connect.jsp" %>
<%
    String id=request.getParameter("id1");
    String name=request.getParameter("name1");
    String gmail1=request.getParameter("gmail1");
    String psw1=request.getParameter("psw1");
    String num1=request.getParameter("num1");
    String doj=request.getParameter("doj");
    String dob=request.getParameter("dob");

    String sql="update staff set email='"+gmail1+"',password='"+psw1+"',contact='"+num1+"',doj='"+doj+"',dob='"+dob+"' where staffid="+id;
    System.out.println("Sql "+sql);
    st.executeUpdate(sql);
%>
<script>
    window.alert("Staff Updated Sucessfully..");
    window.location.assign("viewStaff.jsp");
</script>