import java.util.*;
import org.checkerframework.checker.nullness.qual.Nullable;

class errorArray
{
    public static void main(String[] args)
    {
        int[] arr = {1,2,3,4,5};
        System.out.println(arr[6]);
    }
    void foo(Object nn, @Nullable Object nbl) 
    {
        nn.toString(); // OK
        nbl.toString(); // Error
    }
};
