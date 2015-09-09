package com.Q1;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;
import java.text.SimpleDateFormat;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.math.BigInteger;
import java.util.HashMap;
/**
 * Servlet implementation class FirstServelet
 */
//@WebServlet(description = "q1", urlPatterns = { "/q1" , "/q1.do"}, initParams = {@WebInitParam(name="id",value="1"),@WebInitParam(name="name",value="pankaj")})
public class Q1 extends HttpServlet {
	private static final long serialVersionUID = 1L;
    
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Q1() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HashMap<BigInteger,BigInteger> hs=new HashMap<BigInteger,BigInteger> ();
		BigInteger X = new BigInteger("6876766832351765396496377534476050002970857483815262918450355869850085167053394672634315391224052153");
		BigInteger bign = new BigInteger(request.getParameter("key"));
		boolean a = hs.containsKey(bign);
		BigInteger y;
		if (a==false){
			y = bign.divide(X);
			hs.put(bign, y);
		}else{
			y=(BigInteger)hs.get(bign);
		}
		SimpleDateFormat date = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        response.setContentType("text/plain;charset=US-ASCII");
        PrintWriter out = new PrintWriter(response.getOutputStream());
        out.println(y);
        out.println("Uncle_Cat, 2538-7447-2180, 3207-1716-8663, 4769-4709-3812");
        out.println(date.format(new Date()));
        out.flush();
        out.close();
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}
