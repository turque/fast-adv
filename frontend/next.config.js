/** @type {import('next').NextConfig} */
const nextConfig = {
  // rewrites: async () => {
  //   return [
  //     {
  //       source: "/api/:path*",
  //       destination:
  //         process.env.NODE_ENV === "development"
  //           ? "http://127.0.0.1:8000/api/:path*"
  //           : "/api/",
  //     },
  //     {
  //       source: "/docs",
  //       destination:
  //         process.env.NODE_ENV === "development"
  //           ? "http://127.0.0.1:8000/docs"
  //           : "/api/docs",
  //     },
  //     {
  //       source: "/openapi.json",
  //       destination:
  //         process.env.NODE_ENV === "development"
  //           ? "http://127.0.0.1:8000/openapi.json"
  //           : "/api/openapi.json",
  //     },
  //     {
  //       source: "reqres.in",
  //       destination:
  //         process.env.NODE_ENV
  //     }
  //   ];
  // },
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'reqres.in',
        port: '',
        pathname: '/img/**',
      },
    ],
  },
};

module.exports = nextConfig;
