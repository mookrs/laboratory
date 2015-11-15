#define MAX_VERTEX_NUM 100
typedef char VertexType;
typedef int EdgeType;

/* 邻接矩阵 */
typedef struct
{
    VertexType vexs[MAX_VERTEX_NUM];
    EdgeType edges[MAX_VERTEX_NUM][MAX_VERTEX_NUM];
    int vexnum, arcnum;
}MGraph;


/* 邻接表 */
/* typedef InfoType int; */
typedef struct ArcNode
{
    int adjvex;
    struct ArcNode *nextarc;
    /* InfoType info; */
}ArcNode;
typedef struct
{
    VertexType data;
    ArcNode *first;
}VNode;
typedef struct
{
    VNode vertices[MAX_VERTEX_NUM];
    int vexnum, arcnum;
}ALGraph;


/* 十字链表，有向图 */
/* typedef InfoType int; */
typedef struct ArcNode
{
    int tailvex, headvex;
    struct ArcNode *hlink, tlink;
    /* InfoType info; */
}ArcNode;
typedef struct VNode
{
    VertexType data;
    ArcNode *firstin, *firstout;
}VNode;
typedef struct
{
    VNode xlist[MAX_VERTEX_NUM];
    int vexnum, arcnum;
}GLGraph;


/* 邻接多重表，无向图 */
/* typedef InfoType int; */
typedef struct ArcNode
{
    int mark;
    int ivex, jvex;
    struct ArcNode *ilink, *jlink;
    /* InfoType info; */
}ArcNode;
typedef struct VNode
{
    VertexType data;
    ArcNode *firstedge;
}VNode;
typedef struct
{
    VNode adjmulist[MAX_VERTEX_NUM];
    int vexnum, arcnum;
}AMLGraph;



/* BFS，广度优先搜索 */
int visited[MAX_VERTEX_NUM];
bool visited[MAX_VERTEX_NUM];   /* 用于伪代码 */

void BFSTraverse(ALGraph *G)
{
    int i;

    for (i = 0; i < G->vexnum; ++i)
        visited[i] = 0;

    for (i = 0; i < G->vexnum; ++i)
        if (visited[i] == 0)
            BFS(G, i);
}

/* 伪代码 */
void BFS(Graph G, int v)
{
    int w;
    InitQueue(Q);   /* 这句本来是放在BFSTraverse()中的 */
    
    visit(v);
    visited[v] = TRUE;
    Enqueue(Q, v);
    while(!isEmpty(Q))
    {
        Dequeue(Q, v);
        for (w = FirstNeighbor(G, v); w >= 0; w = NextNeighbor(G, v, w))
        {
            if (!visited[w])
            {
                visit(w);
                visited[w] = 1;
                Enqueue(Q, w);
            }
        }
    }
}

/* 以邻接表为存储结构的广度优先搜索 */
void BFS(ALGraph *G, int v)
{
    ArcNode *p; 
    int queue[MAX_VERTEX_NUM], front = 0, rear = 0;
    int j;

    visit(v);
    visited[v] = 1;

    rear = （rear + 1) % MAX_VERTEX_NUM;
    queue[rear] = v;

    while(front != rear)
    {
        front = (front + 1) % MAX_VERTEX_NUM;
        j = queue[front];

        p = G->vertices[j].first;
        while(p != NULL)
        {
            if(visited[p->adjvex] == 0)
            {
                visit(p->adjvex);
                visited[p->adjvex] = 1;

                rear = (rear + 1) % MAX_VERTEX_NUM;
                queue[rear] = p->adjvex;
            }
            p = p->nextarc;
        }
    }
}



/* DFS，深度优先搜索 */
int visited[MAX_VERTEX_NUM];
bool visited[MAX_VERTEX_NUM];   /* 用于伪代码 */

void DFSTraverse(ALGraph *G)
{
    int i;

    for (i = 0; i < G->vexnum; ++i)
        visited[i] = 0

    for (i = 0; i < G->vexnum; ++i)
        if (visited[i] == 0)
            DFS(G, i);
}

/* 伪代码 */
void DFS(Graph G, int v)
{
    int w;

    visit(v);
    visited[v] = TRUE;
    for (w = FirstNeighbor(G, v); w >= 0; w = NextNeighbor(G, v, w))
    {
        if (!visited[w])
            DFS(G, w);
    }
}

/* 以邻接表为存储结构的深度优先搜索 */
void DFS(ALGraph *G, int v)
{
    ArcNode *p;

    visit(v);
    visited[v] = 1;

    p = G->vertices[v].first;
    while(p != NULL)
    {
        if (visited[p->adjvex] == 0)
            DFS(G, p->adjvex);
        p = p->nextarc;
    }
}



/* BFS算法求解单源最短路径问题，伪代码 */
/* 顶点u到顶点v的最短路径 */
void BFS_MIN_Distance(Graph G, int u)
{
    int i, w;

    for (i = 0; i < G.vexnum; ++i)
        d[i] = INFINITY;    /* 由u到i顶点的最短路径 */

    visited[u] = TRUE;
    d[u] = 0;

    Enqueue(Q, u);
    while(!isEmpty(Q))
    {
        Dequeue(Q, u);  /* 以下for循环的所有顶点w，都和此处出栈的顶点u相关 */
        for (w = FirstNeighbor(G, u); w >= 0; w = NextNeighbor(G, u, w))
        {
            if (!visited[w])
            {
                visited[w] = TRUE;
                d[w] = d[u] + 1;    /* 路径长度加1 */
                Enqueue(Q, w);
            }
        }
    }
}



/* Prim（普里姆）算法 */
/* 伪代码 */
void Prim(G, T) /* 图G=(V, E) */
{
    T = ∅;                  /* 初始化空树 */
    U = {w};                /* 添加任一顶点w */ 
    while((V-U) != ∅)       /* 若树中不包含全部顶点 */
    {
        /* 设(u, v) 是使u∈U与v∈(V-U)，且权值最小的边*/
        T = T ∪ {(u, v)};   /* 边归入树 */
        U = U ∪ {v};        /* 顶点归入树 */
    }
}

void Prim(MGraph *G, int v0)
{
    int lowcost[MAX_VERTEX_NUM];    /* 相关顶点边的权值 */
    int vset[MAX_VERTEX_NUM];
    int i, j, k, min;

    vset[v0] = 1;
    for (i = 1; i < G->vexnum; ++i)
    {
        lowcost[i] = G->edges[v0][i];
        vset[i] = 0;
    }
    
    for (i = 1; i < G->vexnum; ++i)
    {
        min = INFINITY;         /* 初始化最小权值为无穷大 */

        for (j = 1; j < G->vexnum; ++j)
        {
            if (vset[j] == 0 && lowcost[j] < min)
            {
                min = lowcost[j];
                k = j;
            }
        }
        vset[k] = 1;    /* 此顶点已完成任务 */
        /* 此处可计算权值 sum += min; */

        /* 以刚并入的顶点作为媒介更新候选边 */
        for (j = 1; j < G->vexnum; ++j)
        {
            if (vset[j] == 0 && G->edges[k][j] < lowcost[j])
                lowcost[j] = G->edges[k][j];
        }
    }
}



/* Kruskal（克鲁斯卡尔）算法 */
/* 伪代码 */
void Kruskal(V, T)
{
    T = V;              /* 初始化树T，仅含顶点 */
    numS = n;           /* 不连通分量数 */
    while(numS > 1)
    {
        /* 从E中去除权值最小的边(v, u) */
        if (v和u属于T中不同的连通分量)
        {
            T = T ∪ {(v, u)};    /* 将此边加入生成树中 */
            numS--;             /* 不连通分量数减1 */
        }
    }
}

/* 实际就是边集数组 */
typedef struct
{
    int begin, end;
    int weight;
}Edge;

/* 这里的写法是大话数据结构的，天勤定义了一个全局数组road[MAX_VERTEX_NUM] */
void get_root(int *parent, int f)
{
    while(parent[f] > 0)
        f = parent;
    return f;
}


#define MAX_EDGE_NUM 20
void Kruskal(Graph *G)
{
    int i, m, n;
    Edge edges[MAX_EDGE_NUM];
    int parent[MAX_VERTEX_NUM];

    for (i = 0; i < G->vexnum; ++i)
        parent[i] = 0;

    for (i = 0; i < G->arcnum; ++i)
    {
        m = get_root(parent, edges[i].begin);
        n = get_root(parent, edges[i].end);
        if (m != n) /* 说明此边没有与现有生成树形成环路 */
        {
            parent[n] = m;
            printf("(%d, %d) %d\n", edges[i].begin, edges[i].end, edges[i].weight);
            /* sum += edges[i].weight */
        }
}

}