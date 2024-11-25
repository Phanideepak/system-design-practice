import java.util.*;
import java.io.*;


class DatabaseConnection{

    private static DatabaseConnection databaseConnection;

    public static DatabaseConnection getConnection(){

        if(Objects.nonNull(databaseConnection)){
            return databaseConnection;
        }
        return databaseConnection;
    }

    private DatabaseConnection(){
         
    }
}

public class SingletonDemo{
    public static void main(String[] args) {
        DatabaseConnection conn = DatabaseConnection.getConnection();
    }
}

