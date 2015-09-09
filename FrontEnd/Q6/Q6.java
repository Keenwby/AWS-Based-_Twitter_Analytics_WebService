package com.Q6;

import java.io.IOException;
import java.io.PrintWriter;
import java.math.BigInteger;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.sql.*;

/**
 * Servlet implementation class query2
 */
//@WebServlet("/q2")
public class Q6 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Q6() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String ID1 = request.getParameter("m").toString();
		String ID2 = request.getParameter("n").toString();

	

        //System.out.println(time);

		
		Connection conn = null;
		Statement st = null;
		
		try{
			Class.forName("com.mysql.jdbc.Driver");
		}catch(Exception ex){
			System.out.println("Driver error!\n");
		}

		try{
			conn = DriverManager.getConnection("jdbc:mysql://localhost/test?user=root&password=root");
			//System.out.println(conn == null);
		}catch(SQLException ex){
			System.out.println("SQLException: " + ex.getMessage());
		    System.out.println("SQLState: " + ex.getSQLState());
		    System.out.println("VendorError: " + ex.getErrorCode());
		}
		
		
		try{
			st = conn.createStatement();
			
			String query1 = "SELECT return_value FROM q6 WHERE user_id< "+ ID1 + " order by user_id desc limit 1;";
			String query2 = "SELECT return_value FROM q6 WHERE user_id<= "+ ID2 + " order by user_id desc limit 1;";
			//System.out.println(query1);
			//System.out.println(query2);
			
			//execute the first query
			ResultSet rs1 = st.executeQuery(query1);
			response.setContentType("text/plain");
            response.setContentType("charset=UTF-8");
            response.setCharacterEncoding("UTF-8");
			
			PrintWriter pr = new PrintWriter(response.getOutputStream());
			pr.println("Uncle_cat,2538-7447-2180,3207-1716-8663,4769-4709-3812");
			
			int return_value1 = 0;
			while (rs1.next()){
				return_value1 = Integer.parseInt(rs1.getString("return_value"));				
			}
			pr.flush();
			rs1.close();
          
			//execute the second query
			ResultSet rs2 = st.executeQuery(query2);
			response.setContentType("text/plain");
            response.setContentType("charset=UTF-8");
            response.setCharacterEncoding("UTF-8");
			
            int return_value2 = 0;
			while (rs2.next()){
				return_value2 = Integer.parseInt(rs2.getString("return_value"));				
			}
			rs2.close();
			
			int subtraction = return_value2-return_value1;
			pr.println(subtraction);
			pr.flush();
			st.close();
			conn.close();
			
		}catch(SQLException ex){
			// handle any errors
		    System.out.println("SQLException 222: " + ex.getMessage());
		    System.out.println("SQLState: " + ex.getSQLState());
		    System.out.println("VendorError: " + ex.getErrorCode());
			
		}finally{}
		
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}
