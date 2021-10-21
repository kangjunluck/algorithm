package javatest;

import java.util.*;
import java.io.*;

public class network {
	static class data implements Comparable<data> {
		int s, e, w;
		public data(int s, int e, int w) {
			this.s = s;
			this.e = e;
			this.w = w;
		}
		@Override
		public int compareTo(data o) {
			return this.w-o.w;
		}
	}
	static int N;
	static int M;
	static int[] parent;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		parent = new int[N+1];
		for (int i=1; i<=N; i++) {
			parent[i] = i;
		}
		PriorityQueue<data> pq = new PriorityQueue<data>();
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			
			pq.offer(new data(s, e, w));
		}
		int ans = 0;
		int j = 0;
		while(!pq.isEmpty()) {
			data now = pq.poll();
			if (now.s == now.e) continue;
			if (find(now.s) != find(now.e)) {
				j++;
				union(now.s, now.e);
				ans += now.w;
			}
		}
		System.out.println(ans);
	}
	
	static int find(int a) {
		if(parent[a] == a) return a;
		parent[a] = find(parent[a]);
		return parent[a];
	}
	
	static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a > b) {
			parent[a] = b;
		}
		else {
			parent[b] = a;
		}
	}

}
