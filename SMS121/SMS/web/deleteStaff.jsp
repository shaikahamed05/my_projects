<%@include file="connect.jsp" %>

<%
  String sid=request.getParameter("sid");
  String sql="delete from staff where staffid="+sid;
  st.executeUpdate(sql);
  response.sendRedirect("viewStaff.jsp");
%>