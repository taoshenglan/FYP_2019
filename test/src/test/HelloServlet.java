package test;


import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HelloServlet
 */
@WebServlet("/HelloServlet")
public class HelloServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HelloServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		System.out.println("=============");
		String num = request.getParameter("number");
		System.out.println("num:"+num);
		String[] cmdStr_win ={"E:\\school\\comp\\FYP\\TSL\\code\\a.exe",num};
		  

		 try{
			 
			 Process proc = Runtime.getRuntime().exec(cmdStr_win);
			 proc.waitFor();
			
				PrintWriter out = response.getWriter();
				 System.out.println("Success!");
				 String rep = num+" is received!";
				out.append(rep);
				out.flush();
				out.close();

		 }catch(Exception e){
			 e.printStackTrace();
		 }
		
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
