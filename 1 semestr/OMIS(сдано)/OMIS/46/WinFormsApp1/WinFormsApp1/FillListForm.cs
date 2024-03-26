using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormsApp1
{
    
    public partial class FillListForm : Form
    {
        RecordList recordList;
        public FillListForm(RecordList recordList)
        {
            InitializeComponent();
            this.recordList = recordList;
        }

        private void AddElementButton_Click(object sender, EventArgs e)
        {
            recordList.AddRecord(new Group(GroupName.Text, GroupLeader.Text, int.Parse(GroupCount.Text)));
            Close();
        }
    }
}
