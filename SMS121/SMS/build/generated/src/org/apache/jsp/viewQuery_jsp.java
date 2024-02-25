package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.sql.*;

public final class viewQuery_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  static {
    _jspx_dependants = new java.util.ArrayList<String>(1);
    _jspx_dependants.add("/connect.jsp");
  }

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write('\n');
      out.write('\n');

    
    Class.forName("com.mysql.jdbc.Driver");
    Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/sms","root","");
    Statement st=con.createStatement();

      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("<head>\n");
      out.write("<style>\n");
      out.write("ul {\n");
      out.write("  list-style-type: none;\n");
      out.write("  margin: 0;\n");
      out.write("  padding: 0;\n");
      out.write("  overflow: hidden;\n");
      out.write("  background-color: #333;\n");
      out.write("}\n");
      out.write("\n");
      out.write("li {\n");
      out.write("  float: left;\n");
      out.write("  border-right:1px solid #bbb;\n");
      out.write("}\n");
      out.write("\n");
      out.write("li:last-child {\n");
      out.write("  border-right: none;\n");
      out.write("}\n");
      out.write("\n");
      out.write("li a {\n");
      out.write("  display: block;\n");
      out.write("  color: white;\n");
      out.write("  text-align: center;\n");
      out.write("  padding: 14px 16px;\n");
      out.write("  text-decoration: none;\n");
      out.write("}\n");
      out.write("\n");
      out.write("li a:hover:not(.active) {\n");
      out.write("  background-color: #111;\n");
      out.write("}\n");
      out.write("\n");
      out.write(".active {\n");
      out.write("  background-color: #04AA6D;\n");
      out.write("}\n");
      out.write("</style>\n");
      out.write("</head>\n");
      out.write("<body>\n");
      out.write("<center><h1>Student Management System</h1></center>\n");
      out.write("<ul>\n");
      out.write("    <li><a class=\"active\" href=\"AdminHomePage.jsp\">Home</a></li>\n");
      out.write("  <li><a href=\"addStaff.jsp\">AddStaff</a></li>\n");
      out.write("  <li><a href=\"viewStaff.jsp\">ViewStaff</a></li>\n");
      out.write("  <li><a href=\"addStudent.jsp\">AddStudent</a></li>\n");
      out.write("  <li><a href=\"viewStudent.jsp\">ViewStudent</a></li>\n");
      out.write("  <li style=\"float:right\"><a href=\"home.html\">Logout</a></li>\n");
      out.write("</ul>\n");
      out.write("<center><h2>Student Details</h2></center>\n");
      out.write("        ");

            ResultSet rs=st.executeQuery("Select * from query where result is null");
            ResultSetMetaData rsmd=rs.getMetaData();
            int cc=rsmd.getColumnCount();
            
      out.write("\n");
      out.write("            <table width=1000 align=\"center\" border=\"1\" style=\"background-color: powderblue;\">\n");
      out.write("                <tr>\n");
      out.write("                    ");

                        for(int i=1;i<=cc;i++)
                        {
                            
      out.write("\n");
      out.write("                            <td>");
      out.print(rsmd.getColumnLabel(i));
      out.write(" </td>\n");
      out.write("                            ");

                        }
                         
      out.write("\n");
      out.write("                         <td>Update</td><td>Delete</td>\n");
      out.write("                         ");

                        while(rs.next())
                        {
                            
      out.write("\n");
      out.write("                            <tr>\n");
      out.write("                                    ");

                                for(int i=1;i<=cc;i++)
                                {
                                    
      out.write("\n");
      out.write("                                    <td>");
      out.print(rs.getString(i));
      out.write(" </td>\n");
      out.write("                                    ");

                                }
                                 
      out.write("\n");
      out.write("                                 <td><a href=\"updateQuery.jsp?qid=");
      out.print(rs.getString(1));
      out.write("\">Answer</a></td>\n");
      out.write("                                 \n");
      out.write("                            </tr>\n");
      out.write("                            ");

                        }
                        
      out.write("\n");
      out.write("                </tr>\n");
      out.write("                \n");
      out.write("            </table>\n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
