package com.Q5;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.sql.*;

/**
 * Servlet implementation class query2
 */
//@WebServlet("/q2")
public class Q5 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Q5() {
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
			
			String query1 = "SELECT * FROM q5 WHERE user_id= "+ "\"" + ID1 + "\"" +";";
			String query2 = "SELECT * FROM q5 WHERE user_id= "+ "\"" + ID2 + "\"" +";";
			//System.out.println(query);
			
			//excute the first query
			ResultSet rs1 = st.executeQuery(query1);
			response.setContentType("text/plain");
            response.setContentType("charset=UTF-8");
            response.setCharacterEncoding("UTF-8");
			
			PrintWriter pr = new PrintWriter(response.getOutputStream());
			pr.println("Uncle_cat,2538-7447-2180,3207-1716-8663,4769-4709-3812");
			
			int mscore1=0;
			int mscore2=0;
			int mscore3=0;
			int mscore=0;
			
			while (rs1.next()){
				mscore1 = Integer.parseInt(rs1.getString("score1").toString());
				mscore2 = Integer.parseInt(rs1.getString("score2").toString());
				mscore3 = Integer.parseInt(rs1.getString("score3").toString());
				mscore = Integer.parseInt(rs1.getString("score").toString());				
			}
			pr.flush();
			rs1.close();
			
			//execute the second query
			ResultSet rs2 = st.executeQuery(query2);
			response.setContentType("text/plain");
            response.setContentType("charset=UTF-8");
            response.setCharacterEncoding("UTF-8");
            
            int nscore1=0;
			int nscore2=0;
			int nscore3=0;
			int nscore=0;	
			while (rs2.next()){
				nscore1 = Integer.parseInt(rs2.getString("score1").toString());
				nscore2 = Integer.parseInt(rs2.getString("score2").toString());
				nscore3 = Integer.parseInt(rs2.getString("score3").toString());
				nscore = Integer.parseInt(rs2.getString("score").toString());	
			}
			pr.println(ID1+'\t'+ID2+'\t'+"WINNER");
			/*
			 * Score1
			 */
			if(mscore1>nscore1){
				pr.print(mscore1);
				pr.print('\t');
				pr.print(nscore1);
				pr.print('\t');
				pr.println(ID1);
			}else if(mscore1==nscore1){
				pr.print(mscore1);
				pr.print('\t');
				pr.print(nscore1);
				pr.print('\t');
				pr.println("X");
			}else{
				pr.print(mscore1);
				pr.print('\t');
				pr.print(nscore1);
				pr.print('\t');
				pr.println(ID2);
			}
			/*
			 * Score2
			 */
			if(mscore2>nscore2){
				pr.print(mscore2);
				pr.print('\t');
				pr.print(nscore2);
				pr.print('\t');
				pr.println(ID1);
			}else if(mscore2==nscore2){
				pr.print(mscore2);
				pr.print('\t');
				pr.print(nscore2);
				pr.print('\t');
				pr.println("X");
			}else{
				pr.print(mscore2);
				pr.print('\t');
				pr.print(nscore2);
				pr.print('\t');
				pr.println(ID2);
			}
			/*
			 * Score3
			 */
			if(mscore3>nscore3){
				pr.print(mscore3);
				pr.print('\t');
				pr.print(nscore3);
				pr.print('\t');
				pr.println(ID1);
			}else if(mscore3==nscore3){
				pr.print(mscore3);
				pr.print('\t');
				pr.print(nscore3);
				pr.print('\t');
				pr.println("X");
			}else{
				pr.print(mscore3);
				pr.print('\t');
				pr.print(nscore3);
				pr.print('\t');
				pr.println(ID2);
			}
			/*
			 * overall score
			 */
			if(mscore>nscore){
				pr.print(mscore);
				pr.print('\t');
				pr.print(nscore);
				pr.print('\t');
				pr.println(ID1);
			}else if(mscore==nscore){
				pr.print(mscore);
				pr.print('\t');
				pr.print(nscore);
				pr.print('\t');
				pr.println("X");
			}else{
				pr.print(mscore);
				pr.print('\t');
				pr.print(nscore);
				pr.print('\t');
				pr.println(ID2);
			}
			pr.flush();
			rs2.close();
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
