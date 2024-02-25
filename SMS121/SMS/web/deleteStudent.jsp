<%@include file="connect.jsp" %>

<%
  String sid=request.getParameter("sid");
  String sql="delete from student where studentid="+sid;
  st.executeUpdate(sql);
  response.sendRedirect("viewStudent.jsp");
%>