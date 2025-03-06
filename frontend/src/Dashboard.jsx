import Layout from "../components/Layout";
import Card from "../components/Card";
import Button from "../components/Button";

export default function Dashboard() {
  return (
    <Layout>
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
      <Card title="Dados">
        <p>Aqui vai um resumo dos dados.</p>
        <Button onClick={() => alert("Clicado!")}>Ver mais</Button>
      </Card>
    </Layout>
  );
}
