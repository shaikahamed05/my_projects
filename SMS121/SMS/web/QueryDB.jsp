<%@include file="connect.jsp" %>
<%
    String q=request.getParameter("q");
    
    
    String sql="insert into query(query) values('"+q+"')";
    st.executeUpdate(sql);
%>
<script>
    window.alert("Query added Sucessfully..");
    window.location.assign("StudentHomePage.jsp");
</script>