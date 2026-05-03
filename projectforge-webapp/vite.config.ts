/// <reference types="vitest/config" />
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { transformSync } from 'esbuild';

function rruleJsxPlugin() {
    return {
        name: 'rrule-jsx',
        enforce: 'pre',
        transform(src, id) {
            if (id.endsWith('.js') && (
                id.includes('react-rrule-generator') ||
                (id.includes('node_modules') && /<[A-Z]\w*[\s/>]/.test(src))
            )) {
                const result = transformSync(src, {
                    loader: 'jsx',
                    format: 'cjs',
                    target: 'esnext',
                });
                return result.code;
            }
        },
    };
}

export default defineConfig({
    plugins: [rruleJsxPlugin(), react()],
    publicDir: 'public',
    css: {
        preprocessorOptions: {
            scss: {
                loadPaths: ['./node_modules'],
            },
        },
    },
    build: {
        outDir: 'build',
        sourcemap: false,
        minify: false,
        rollupOptions: {
            maxParallelFileOps: 1,
        },
    },
    server: {
        port: 3000,
        proxy: {
            '/rs': {
                target: 'http://localhost:8080',
                changeOrigin: true,
            },
            '/rest': {
                target: 'http://localhost:8080',
                changeOrigin: true,
            },
        },
    },
    test: {
        environment: 'jsdom',
        globals: true,
        include: ['src/**/*.{test,spec}.{js,jsx,ts,tsx}'],
        exclude: ['**/ProjectForge.test.jsx'],
    },
});