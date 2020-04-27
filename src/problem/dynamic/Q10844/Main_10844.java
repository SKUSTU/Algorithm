package problem.dynamic.Q10844;
import java.io.*;

public class Main_10844 {
    public static int mod = 1000000000;
    public static int n;
    public static int[][] d;
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        d = new int[n+1][10];
        long answer = solve(n);
        bw.write(Long.toString(answer));
        bw.flush();
        bw.close();
    }
    public static long solve(int n){
        long answer = 0;
        for(int i=1; i<=9; i++){
            d[1][i] = 1;        //1개 짜리 계단수  1/2/3/4/5/6/7/8/9
        }
        for(int i=2; i<=n; i++) {
            for(int j=0; j<=9; j++){
                if(j+1 <= 9){
                    d[i][j] += d[i-1][j+1];
                }
                if(j-1 >= 0){
                    d[i][j] += d[i-1][j-1];
                }
                d[i][j] %= mod;
            }
        }
        for(int i=0; i<=9; i++){
            answer += d[n][i];
        }
        return answer%mod;
    }
}
