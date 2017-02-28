

public class Problem24 {
    private static int n = 0, N;
    public static void main(String[] args) {
        N = Integer.parseInt(args[0]);
        permutate(args[1], new boolean[args[1].length()], new StringBuffer());
    }

    private static void permutate(String in, boolean[] used, StringBuffer sb) {
        if(sb.length() == in.length()) {
            if(++n == N) {
                System.out.println(sb);
            }
            return;
        }
        for(int i = 0; i < in.length(); i++) {
            if(!used[i]) {
                used[i] = true;
                sb.append(in.charAt(i));
                permutate(in, used, sb);
                sb.deleteCharAt(sb.length() - 1);
                used[i] = false;
            }
        } 
    }
}
