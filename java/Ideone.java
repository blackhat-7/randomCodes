import java.util.stream.IntStream;
import java.util.stream.Stream;

class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Stream<double[]> h = IntStream.rangeClosed(1,100).boxed().flatMap(a -> IntStream.rangeClosed(a,10).mapToObj(b -> new double[] {a,b,Math.sqrt(a*a+b*b)}).filter (t->t[2]%1==0));
        h.limit(5).forEach(t->System.out.println(t[0]+", "+t[1]+", "+t[2]));
        
	}
}