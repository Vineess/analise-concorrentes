export default function Card({ title, children }) {
    return (
      <div className="bg-white shadow-lg rounded-lg p-4">
        <h3 className="text-lg font-bold mb-2">{title}</h3>
        {children}
      </div>
    );
  }
  