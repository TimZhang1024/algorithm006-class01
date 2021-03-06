# 学习笔记
## 第十三课 字典树和并查集

### Tries树

- 又称单词查找树或者键树
- 核心思想是空间换时间
- 典型应用

	- 统计
	- 排序大量字符串（不局限于字符串）

- 优点

	- 减少无谓的字符串比较
	- 查询效率比哈希表高

- 基本性质

	- 结点本身不存完整单词，可存储其他信息如统计次数等
	- 从根节点到某一结点，路径上经过的字符连接起来，就是该结点对应的字符串
	- 每个结点所有子节点代表的字符串不同

- 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的

### 并查集

- 适用场景

	- 组团、配对问题
	- Group or not

- 基本操作

	- makeSet(s)

		- 建立一个新的并查集，其中包含s个单元素集合

	- unionSet(x, y)

		- 把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并

	- find(x)

		- 找到元素x所在的集合的代表
		- 也可以用于判断两个元素是否位于同一个集合内

- 模板代码

  ```java
  class UnionFind { 
    	private int count = 0; 
    	private int[] parent; 
    	public UnionFind(int n) { 
    		count = n; 
    		parent = new int[n]; 
    		for (int i = 0; i < n; i++) { 
    			parent[i] = i;
    		}
    	} 
    	public int find(int p) { 
    		while (p != parent[p]) { 
    			parent[p] = parent[parent[p]]; 
    			p = parent[p]; 
    		}
    		return p; 
    	}
    	public void union(int p, int q) { 
    		int rootP = find(p); 
    		int rootQ = find(q); 
    		if (rootP == rootQ) return; 
    		parent[rootP] = rootQ; 
    		count--;
    	}
    }
  ```

## 第十四课 高级搜索

### 初级搜索

- 朴素搜索

	- 暴力
	- 重复

- 优化方式

	- 不重复运算，记忆化

		- 斐波那契数列

	- 剪枝

		- 括号生成

	- 搜索方向优化

		- 双向搜索
		- 启发式搜索

### 剪枝

- 在预计不能达到最终目标时，提前结束本次及后续处理
- 降低状态树复杂度
- 括号生成

	- 判断当前次生成括号是否合法，不合法不进行后续生成
	- 左括号始终可以放，只要小于目标
	- 右括号只有在小于左括号数目，且小于目标时才可以

- 数独填充问题

	- 值得学习的实现方式

		- 反向思维，得到数独空位可用数字，递归处理，可用数字归0即可行，没有归0说明不可行

### 双向BFS

- 相对于传统BFS方式优化
- 一侧从根节点开始，一侧从目标节点开始，直到双向相遇停止
- 单词搜索

	- 方向1

		- 从beginword开始

	- 方向2

		- 从endword开始

	- 两者的队列有相交元素时停止

### 启发式搜索

- 又叫A*搜索、优先级搜索、智能搜索
- 根据某一项条件，不断优化搜索方向
- 估价函数、优先级函数、启发式函数

	- 用来评价哪些结点最有希望的是一个要找的结点
	- 返回一个非负实数，代表查找结点的代价
	- 

- 各种距离计算方式

	- 坐标值之差的绝对值之和
	- 汉明距离
	- 曼哈顿距离

## 第十五课 红黑树和AVL树

### AVL树

- 防止二叉搜索树极端情况下退化为链表的情况
- 保证左右子树平衡
- 关键概念

	- 平衡因子（Balance Factor）

		- -1
		- 0
		- 1

	- 四种旋转操作

- 旋转操作

	- 左旋

		- 右右子树的情况

		  A
		  	B
		  		C

	- 右旋

		- 左左子树的情况

		  A
		  	B
		  C

	- 左右旋

		- 左右子树的情况

		  A
		  	B
		  		C

	- 右左旋

		- 右左子树的情况

		  A
		  	B
		  C

- 不足

	- 需要存储额外信息
	- 调整次数频繁

### 红黑树

- 近似平衡的二叉搜索树，任何一个结点的左右子树的高度差小于两倍
- 满足如下条件的二叉搜索树

	- 每个结点要么是红色，要么是黑色
	- 根结点是黑色
	- 每个叶结点是黑色的，且是空结点
	- 不能有相邻接的两个红色结点
	- 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点

### 两者对比

- AVL树因为严格平衡，查找效率比红黑树更高一点
- 红黑树的插入、删除速度超过AVL树，因为减少了达到平衡的旋转
- AVL树需要存储结点额外信息，比红黑树占用多一点额外空间
- 红黑树在多数语言中均有库实现，AVL树多用于DB中

