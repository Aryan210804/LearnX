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

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
