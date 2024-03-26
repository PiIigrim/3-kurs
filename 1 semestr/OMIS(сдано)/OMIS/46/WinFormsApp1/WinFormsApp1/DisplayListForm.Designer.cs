namespace WinFormsApp1
{
    partial class OneToOne
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
            colorDialog1 = new ColorDialog();
            GroupNameRO = new TextBox();
            GroupName = new TextBox();
            GroupLeaderRO = new TextBox();
            GroupLeader = new TextBox();
            GroupCountRO = new TextBox();
            GroupCount = new TextBox();
            ToLeft = new Button();
            IndexGroup = new TextBox();
            ToRight = new Button();
            ToEndLeft = new Button();
            ToEndRight = new Button();
            SuspendLayout();
            // 
            // GroupNameRO
            // 
            GroupNameRO.Location = new Point(12, 67);
            GroupNameRO.Name = "GroupNameRO";
            GroupNameRO.ReadOnly = true;
            GroupNameRO.Size = new Size(150, 31);
            GroupNameRO.TabIndex = 0;
            GroupNameRO.Text = "Имя группы";
            GroupNameRO.TextChanged += textBox1_TextChanged;
            // 
            // GroupName
            // 
            GroupName.Location = new Point(185, 67);
            GroupName.Name = "GroupName";
            GroupName.ReadOnly = true;
            GroupName.Size = new Size(150, 31);
            GroupName.TabIndex = 1;
            // 
            // GroupLeaderRO
            // 
            GroupLeaderRO.Location = new Point(12, 144);
            GroupLeaderRO.Name = "GroupLeaderRO";
            GroupLeaderRO.ReadOnly = true;
            GroupLeaderRO.Size = new Size(150, 31);
            GroupLeaderRO.TabIndex = 2;
            GroupLeaderRO.Text = "Староста";
            // 
            // GroupLeader
            // 
            GroupLeader.Location = new Point(185, 144);
            GroupLeader.Name = "GroupLeader";
            GroupLeader.ReadOnly = true;
            GroupLeader.Size = new Size(150, 31);
            GroupLeader.TabIndex = 3;
            // 
            // GroupCountRO
            // 
            GroupCountRO.Location = new Point(12, 231);
            GroupCountRO.Name = "GroupCountRO";
            GroupCountRO.ReadOnly = true;
            GroupCountRO.Size = new Size(150, 31);
            GroupCountRO.TabIndex = 4;
            GroupCountRO.Text = "Численность";
            // 
            // GroupCount
            // 
            GroupCount.Location = new Point(185, 231);
            GroupCount.Name = "GroupCount";
            GroupCount.ReadOnly = true;
            GroupCount.Size = new Size(150, 31);
            GroupCount.TabIndex = 5;
            // 
            // ToLeft
            // 
            ToLeft.Location = new Point(60, 328);
            ToLeft.Name = "ToLeft";
            ToLeft.Size = new Size(112, 34);
            ToLeft.TabIndex = 6;
            ToLeft.Text = "<";
            ToLeft.UseVisualStyleBackColor = true;
            ToLeft.Click += ToLeft_Click;
            // 
            // IndexGroup
            // 
            IndexGroup.BackColor = SystemColors.Window;
            IndexGroup.Location = new Point(98, 12);
            IndexGroup.Name = "IndexGroup";
            IndexGroup.ReadOnly = true;
            IndexGroup.Size = new Size(150, 31);
            IndexGroup.TabIndex = 7;
            // 
            // ToRight
            // 
            ToRight.Location = new Point(178, 328);
            ToRight.Name = "ToRight";
            ToRight.Size = new Size(112, 34);
            ToRight.TabIndex = 8;
            ToRight.Text = ">";
            ToRight.UseVisualStyleBackColor = true;
            ToRight.Click += ToRight_Click;
            // 
            // ToEndLeft
            // 
            ToEndLeft.Location = new Point(60, 377);
            ToEndLeft.Name = "ToEndLeft";
            ToEndLeft.Size = new Size(112, 34);
            ToEndLeft.TabIndex = 9;
            ToEndLeft.Text = "<<";
            ToEndLeft.UseVisualStyleBackColor = true;
            ToEndLeft.Click += ToEndLeft_Click;
            // 
            // ToEndRight
            // 
            ToEndRight.Location = new Point(178, 377);
            ToEndRight.Name = "ToEndRight";
            ToEndRight.Size = new Size(112, 34);
            ToEndRight.TabIndex = 10;
            ToEndRight.Text = ">>";
            ToEndRight.UseVisualStyleBackColor = true;
            ToEndRight.Click += ToEndRight_Click;
            // 
            // OneToOne
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(347, 450);
            Controls.Add(ToEndRight);
            Controls.Add(ToEndLeft);
            Controls.Add(ToRight);
            Controls.Add(IndexGroup);
            Controls.Add(ToLeft);
            Controls.Add(GroupCount);
            Controls.Add(GroupCountRO);
            Controls.Add(GroupLeader);
            Controls.Add(GroupLeaderRO);
            Controls.Add(GroupName);
            Controls.Add(GroupNameRO);
            Name = "OneToOne";
            Text = "OneToOne";
            Load += OneToOne_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ColorDialog colorDialog1;
        private TextBox GroupNameRO;
        private TextBox GroupName;
        private TextBox GroupLeaderRO;
        private TextBox GroupLeader;
        private TextBox GroupCountRO;
        private TextBox GroupCount;
        private Button ToLeft;
        private TextBox IndexGroup;
        private Button ToRight;
        private Button ToEndLeft;
        private Button ToEndRight;
    }
}