import java.util.*;

class test {
	public static void main(String[] args) {
		List<Integer> lst = new ArrayList<>();
		lst.add(1);
		System.out.println(lst.toArray(new Integer[lst.size()]).toString());
	}
}
