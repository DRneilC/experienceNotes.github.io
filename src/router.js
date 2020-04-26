const routers = [
    {
        path: '/',
        meta: {
            title: ''
        },
        component: (resolve) => require(['./views/index.vue'], resolve)
    },
    {
        path: '/handwriting',
        meta: {
            title: '手写板'
        },
        component: (resolve) => require(['./views/handwriting.vue'], resolve)
    },
    {
        path: '/clocks',
        meta: {
            title: 'canvas时钟'
        },
        component: (resolve) => require(['./views/clocks.vue'], resolve)
    },
    {
        path: '/img-magnifier',
        meta: {
            title: '图片查看器'
        },
        component: (resolve) => require(['./views/img-magnifier.vue'], resolve)
    },
    {
        path: '/img-scale',
        meta: {
            title: '图片缩放'
        },
        component: (resolve) => require(['./views/img-scale.vue'], resolve)
    },
    {
        path: '/line',
        meta: {
            title: 'canvas颗粒吸附'
        },
        component: (resolve) => require(['./views/line.vue'], resolve)
    },
    {
        path: '/christmas',
        meta: {
            title: '圣诞节--雪花'
        },
        component: (resolve) => require(['./views/christmas.vue'], resolve)
    },
];
export default routers;