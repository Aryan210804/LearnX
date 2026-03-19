/**
 * LearnX — Firebase Configuration (ES Module)
 * Shared Firebase initialization for all pages.
 *
 * Usage:
 *   import { auth, db } from '../assets/js/firebase-init.js';
 */
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyDrOAHTg-BuXyDRcBAV3uxoFHUwIzlV3bU",
  authDomain: "learnx-d823d.firebaseapp.com",
  projectId: "learnx-d823d",
  storageBucket: "learnx-d823d.appspot.com",
  messagingSenderId: "1036419202232",
  appId: "1:1036419202232:web:4f7778b3b4c16f1a61084d"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);

/**
 * Handle common Firebase errors and provide user-friendly messages.
 */
export function handleFirebaseError(error) {
  console.error("Firebase Error:", error);
  let msg = error.message || "An unknown error occurred.";
  
  // Strip "Firebase: " prefix if present
  msg = msg.replace("Firebase: ", "");
  
  // Specific handling for common auth errors
  switch (error.code) {
    case "auth/network-request-failed":
      if (window.location.protocol === "file:") {
        return "Network Error: Firebase Authentication often fails when running from a local file (file://). Please use a local server (like Live Server or python -m http.server) or check your internet connection.";
      }
      return "Network Error: Please check your internet connection and try again.";
    case "auth/invalid-email":
      return "The email address is not valid.";
    case "auth/user-disabled":
      return "This user account has been disabled.";
    case "auth/user-not-found":
    case "auth/wrong-password":
    case "auth/invalid-credential":
      return "Invalid email or password. Please try again.";
    case "auth/email-already-in-use":
      return "An account already exists with this email address.";
    case "auth/weak-password":
      return "The password is too weak. Please use at least 6 characters.";
    case "auth/operation-not-allowed":
      return "This authentication method is not enabled in the Firebase Console.";
    default:
      if (msg.includes("network-request-failed")) {
        return "Network Error: Could not connect to the authentication server.";
      }
      return msg;
  }
}


