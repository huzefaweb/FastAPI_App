// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindPostcss from '@tailwindcss/postcss'
import autoprefixer from 'autoprefixer'

export default defineConfig({
  css: {
    postcss: {
      plugins: [ tailwindPostcss(), autoprefixer() ]
    }
  },
  plugins: [react()],
  server: { port: 3000 }
})
