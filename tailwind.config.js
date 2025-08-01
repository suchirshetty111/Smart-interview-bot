/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
      },
      colors: {
        primary: '#2563eb', // Tailwind blue-600
        secondary: '#9333ea', // Tailwind purple-600
      },
      boxShadow: {
        card: '0 4px 12px rgba(0, 0, 0, 0.1)',
      },
    },
  },
  plugins: [],
}
