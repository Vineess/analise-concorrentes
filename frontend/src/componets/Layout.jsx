import { Link } from "react-router-dom";

export default function Layout({ children }) {
  return (
    <div>
      <nav className="bg-blue-600 p-4 text-white flex justify-between">
        <h1 className="text-xl font-bold">Minha Aplicação</h1>
        <div>
          <Link to="/" className="px-4">Home</Link>
          <Link to="/dashboard" className="px-4">Dashboard</Link>
        </div>
      </nav>
      <main className="p-6">{children}</main>
    </div>
  );
}
