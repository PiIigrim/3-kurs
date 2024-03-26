namespace WinFormsApp1
{
    public partial class MainForm : Form
    {
        RecordList recordList;
        public MainForm(string filepath)
        {
            InitializeComponent();
            recordList = new RecordList(filepath);
            recordList.LoadFromFile();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
        }

        public void RewriteDB()
        {
            dataGridView1.Rows.Clear();
            foreach (Group group in recordList.GetGroups())
            {
                dataGridView1.Rows.Add(group.GroupName, group.GroupLeader, group.StudentCount);

            }
        }
        private void dataGridView1_UserDeletingRow(object sender, DataGridViewRowCancelEventArgs e)
        {
            DataGridViewRow row = e.Row;
            textBox1.Text += row.Index.ToString();
            recordList.RemoveRecord(recordList.GetGroups()[row.Index]);
        }
        private void записьЗаЗаписьюToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DisplayListForm oneToOne = new DisplayListForm(recordList.GetGroups());
            oneToOne.Show();

        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void добавитьСписокToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FillListForm addel = new FillListForm(recordList);
            addel.ShowDialog();
            RewriteDB();
        }

        private void поискПервойЗаписиToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SearchRecordForm fm = new SearchRecordForm(recordList.GetGroups());
            fm.ShowDialog();

        }

        private void создатьСписокToolStripMenuItem_Click(object sender, EventArgs e)
        {
            CreateListForm newDB = new CreateListForm(recordList);
            newDB.ShowDialog();
            RewriteDB();
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void открытьсписокToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.Cancel) return;
            IsNeedToSave();
            recordList = new RecordList(openFileDialog1.FileName);
            recordList.LoadFromFile();
            RewriteDB();
        }
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            IsNeedToSave();
        }
        private void IsNeedToSave() {
            if (MessageBox.Show("Хотите сохранить изменения?", "Внимание", MessageBoxButtons.YesNo) == DialogResult.Yes)
            {recordList.SaveToFile();}
            else{;}
        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}