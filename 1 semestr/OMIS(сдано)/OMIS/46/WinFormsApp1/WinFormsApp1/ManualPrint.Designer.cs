namespace WinFormsApp1
{
    partial class ManualPrint
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            dataGridView1 = new DataGridView();
            NameGroup = new DataGridViewTextBoxColumn();
            HeaderGroup = new DataGridViewTextBoxColumn();
            Count = new DataGridViewTextBoxColumn();
            GroupCount = new TextBox();
            GroupLeader = new TextBox();
            GroupName = new TextBox();
            GroupCountRO = new TextBox();
            GroupLeaderRO = new TextBox();
            GroupNameRO = new TextBox();
            AddElButton = new Button();
            SaveTableButton = new Button();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            SuspendLayout();
            // 
            // dataGridView1
            // 
            dataGridView1.AllowUserToDeleteRows = false;
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            dataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.AllCells;
            dataGridView1.BackgroundColor = SystemColors.Control;
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Columns.AddRange(new DataGridViewColumn[] { NameGroup, HeaderGroup, Count });
            dataGridView1.Dock = DockStyle.Left;
            dataGridView1.EditMode = DataGridViewEditMode.EditProgrammatically;
            dataGridView1.Location = new Point(0, 0);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.ReadOnly = true;
            dataGridView1.RowHeadersWidth = 62;
            dataGridView1.RowTemplate.Height = 33;
            dataGridView1.Size = new Size(435, 450);
            dataGridView1.TabIndex = 1;
            // 
            // NameGroup
            // 
            NameGroup.HeaderText = "Имя Группы";
            NameGroup.MinimumWidth = 8;
            NameGroup.Name = "NameGroup";
            NameGroup.ReadOnly = true;
            // 
            // HeaderGroup
            // 
            HeaderGroup.HeaderText = "Староста";
            HeaderGroup.MinimumWidth = 8;
            HeaderGroup.Name = "HeaderGroup";
            HeaderGroup.ReadOnly = true;
            // 
            // Count
            // 
            Count.HeaderText = "Численность";
            Count.MinimumWidth = 8;
            Count.Name = "Count";
            Count.ReadOnly = true;
            // 
            // GroupCount
            // 
            GroupCount.Location = new Point(627, 162);
            GroupCount.Name = "GroupCount";
            GroupCount.Size = new Size(150, 31);
            GroupCount.TabIndex = 23;
            // 
            // GroupLeader
            // 
            GroupLeader.Location = new Point(627, 89);
            GroupLeader.Name = "GroupLeader";
            GroupLeader.Size = new Size(150, 31);
            GroupLeader.TabIndex = 22;
            // 
            // GroupName
            // 
            GroupName.Location = new Point(627, 12);
            GroupName.Name = "GroupName";
            GroupName.Size = new Size(150, 31);
            GroupName.TabIndex = 21;
            // 
            // GroupCountRO
            // 
            GroupCountRO.Location = new Point(456, 162);
            GroupCountRO.Name = "GroupCountRO";
            GroupCountRO.ReadOnly = true;
            GroupCountRO.Size = new Size(150, 31);
            GroupCountRO.TabIndex = 20;
            GroupCountRO.Text = "Численность";
            // 
            // GroupLeaderRO
            // 
            GroupLeaderRO.Location = new Point(456, 89);
            GroupLeaderRO.Name = "GroupLeaderRO";
            GroupLeaderRO.ReadOnly = true;
            GroupLeaderRO.Size = new Size(150, 31);
            GroupLeaderRO.TabIndex = 19;
            GroupLeaderRO.Text = "Староста";
            // 
            // GroupNameRO
            // 
            GroupNameRO.Location = new Point(456, 12);
            GroupNameRO.Name = "GroupNameRO";
            GroupNameRO.ReadOnly = true;
            GroupNameRO.Size = new Size(150, 31);
            GroupNameRO.TabIndex = 18;
            GroupNameRO.Text = "Имя группы";
            // 
            // AddElButton
            // 
            AddElButton.Location = new Point(456, 261);
            AddElButton.Name = "AddElButton";
            AddElButton.Size = new Size(150, 65);
            AddElButton.TabIndex = 24;
            AddElButton.Text = "Добавить";
            AddElButton.UseVisualStyleBackColor = true;
            AddElButton.Click += AddElButton_Click;
            // 
            // SaveTableButton
            // 
            SaveTableButton.Location = new Point(627, 261);
            SaveTableButton.Name = "SaveTableButton";
            SaveTableButton.Size = new Size(150, 65);
            SaveTableButton.TabIndex = 25;
            SaveTableButton.Text = "Сохранить";
            SaveTableButton.UseVisualStyleBackColor = true;
            SaveTableButton.Click += SaveTableButton_Click;
            // 
            // ManualPrint
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(SaveTableButton);
            Controls.Add(AddElButton);
            Controls.Add(GroupCount);
            Controls.Add(GroupLeader);
            Controls.Add(GroupName);
            Controls.Add(GroupCountRO);
            Controls.Add(GroupLeaderRO);
            Controls.Add(GroupNameRO);
            Controls.Add(dataGridView1);
            Name = "ManualPrint";
            Text = "ManualPrint";
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private DataGridView dataGridView1;
        private DataGridViewTextBoxColumn NameGroup;
        private DataGridViewTextBoxColumn HeaderGroup;
        private DataGridViewTextBoxColumn Count;
        private TextBox GroupCount;
        private TextBox GroupLeader;
        private TextBox GroupName;
        private TextBox GroupCountRO;
        private TextBox GroupLeaderRO;
        private TextBox GroupNameRO;
        private Button AddElButton;
        private Button SaveTableButton;
    }
}