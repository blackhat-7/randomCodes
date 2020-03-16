/*
 * import
 * load and register the driver --> com.mysql.jdbc.Driver
 * create connection
 * create a statement
 * execute the query
 * process the results
 * close
*/

import java.sql.*;

class Firstapp {

    public static void main(String[] args) throws Exception {
        String url = "jdbc:mariadb://localhost:3306//classicmodelss";
        String uname = "shaun";
        String pass = "astonmartin7";
        String query = "select customerName from customers";

        Class.forName("org.mariadb.jdbc.Driver");
        Connection con = DriverManager.getConnection(url, uname, pass);
        Statement st = con.createStatement();
        ResultSet rs = st.executeQuery(query);

        rs.next();
        String name = rs.getString("customerName");
        System.out.println(name);

        st.close();
        con.close();
    }

}
