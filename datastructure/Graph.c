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
void BFSTraverse(Graph G)
{
    int i;

    for (i = 0; i < G.vexnum; ++i)
        visited[i] = 0;
    InitQueue(Q);
    for (int i = 0; i < G.vexnum; ++i)
        if (!visited[i])
            BFS(G, i);
}

void BFS(Graph G, int v)
{
    int w;
    
    visit(v);
    visited[v] = 1;
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


/* DFS，深度优先搜索 */








