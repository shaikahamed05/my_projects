<%@include file="connect.jsp" %>
<%
    String id=request.getParameter("id");
    
    String ans=request.getParameter("ans");
    
    String sql="update query set result='"+ans+"' where qid="+id;
    System.out.println("Sql "+sql);
    st.executeUpdate(sql);
%>
<script>
    window.alert("Query Updated Sucessfully..");
    window.location.assign("viewQuery.jsp");
</script>