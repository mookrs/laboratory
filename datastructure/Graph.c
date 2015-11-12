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
bool visited[MAX_VERTEX_NUM];   /* 伪代码使用 */

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
bool visited[MAX_VERTEX_NUM];   /* 伪代码使用 */

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



/*  */