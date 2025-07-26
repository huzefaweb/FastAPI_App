import React from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();

  const handleSignOut = async () => {
    const token = localStorage.getItem('access_token');
    try {
      const res = await fetch(
        `${import.meta.env.VITE_API_URL}/auth/signout`,
        {
          method: 'POST',
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      if (!res.ok) console.error('Sign out failed:', res.statusText);
    } catch (err) {
      console.error('Sign out error:', err);
    } finally {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      navigate('/login');
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="min-h-screen flex items-center justify-center bg-gray-50 p-4"
    >
      <div className="max-w-md w-full bg-white rounded-2xl shadow-xl p-8 text-center space-y-6">
        <h1 className="text-4xl font-bold text-gray-800">Welcome!</h1>
        <p className="text-gray-600">
          You’re now signed in. Explore your dashboard or sign out when ready.
        </p>
        <button
          onClick={handleSignOut}
          className="mt-4 px-6 py-3 bg-red-500 text-white font-semibold rounded-lg shadow hover:bg-red-600 transition"
        >
          Sign Out
        </button>
      </div>
    </motion.div>
  );
}
